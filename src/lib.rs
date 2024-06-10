#![feature(portable_simd)]
mod preload;

use std::{
    ops::{BitAndAssign, BitOrAssign, BitXorAssign},
    simd::{self, u32x4, u8x16},
    vec,
};

use pyo3::prelude::*;

// binary storage array struct
#[pyclass]
struct BinaryArray {
    length: usize,
    binary_storage: Vec<u32>,
}

// binary storage array methods callable from python
#[pymethods]
impl BinaryArray {
    #[new]
    fn new(bin_list: Vec<u32>) -> Self {
        Self {
            length: bin_list.len(),
            binary_storage: compress_bin(&bin_list),
        }
    }

    // TODO: make this a one-liner
    fn get_list(&self) -> Vec<u8> {
        let mut v: Vec<u8> = vec![0u8; self.length];
        for i in 0..self.length {
            v[i] = !(self.binary_storage[i / 32] & (1u32 << i % 32) == 0) as u8;
        }
        v
    }

    fn __str__(&self) -> String {
        let v: Vec<u8> = self.get_list();
        format!("{:?}", v)
    }

    fn __getitem__(&self, idx: usize) -> u32 {
        (self.binary_storage[idx / 32] & (1u32 << (idx % 32)) != 0) as u32
    }

    fn __setitem__(&mut self, idx: usize, val: u32) -> () {
        let comp = val << (idx % 32);
        let mask = 1u32 << (idx % 32);
        // TODO: make this use only bitwise operators
        if mask & self.binary_storage[idx / 32] != comp {
            self.binary_storage[idx / 32] ^= mask;
        }
    }

    fn __eq__(&self, other: &BinaryArray) -> bool {
        if self.length != other.length {
            return false;
        }
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *const u32x4 = self.binary_storage.as_ptr() as *const u32x4;
        let p_other: *const u32x4 = other.binary_storage.as_ptr() as *const u32x4;

        for i in 0..chunks {
            unsafe {
                if *p_self.offset(i) != *p_other.offset(i) {
                    return false;
                }
            }
        }
        true
    }

    // takes the bitwise and of the binary array,
    // stores the result in the self operand
    // panics if lengths are not equal
    fn bit_and(&self, other: &BinaryArray) -> () {
        if self.length != other.length {
            panic!(
                "Lengths of binary arrays must be equal in order to take the bitwise and of them."
            );
        }
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *mut u32x4 = self.binary_storage.as_ptr() as *mut u32x4;
        let p_other: *const u32x4 = other.binary_storage.as_ptr() as *const u32x4;

        for i in 0..chunks {
            unsafe {
                (*p_self.offset(i)).bitand_assign(*p_other.offset(i));
            }
        }
    }

    fn bit_or(&self, other: &BinaryArray) -> () {
        if self.length != other.length {
            panic!(
                "Lengths of binary arrays must be equal in order to take the bitwise and of them."
            );
        }
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *mut u32x4 = self.binary_storage.as_ptr() as *mut u32x4;
        let p_other: *const u32x4 = other.binary_storage.as_ptr() as *const u32x4;

        for i in 0..chunks {
            unsafe {
                (*p_self.offset(i)).bitor_assign(*p_other.offset(i));
            }
        }
    }

    fn bit_xor(&self, other: &BinaryArray) {
        if self.length != other.length {
            panic!(
                "Lengths of binary arrays must be equal in order to take the bitwise xor of them."
            );
        }
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *mut u32x4 = self.binary_storage.as_ptr() as *mut u32x4;
        let p_other: *const u32x4 = other.binary_storage.as_ptr() as *const u32x4;

        for i in 0..chunks {
            unsafe {
                (*p_self.offset(i)).bitxor_assign(*p_other.offset(i));
            }
        }
    }

    fn bit_not(&self) {
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *mut u32x4 = self.binary_storage.as_ptr() as *mut u32x4;
        const INV: u32x4 = u32x4::from_array([u32::MAX; 4]);

        for i in 0..chunks {
            if i != chunks - 1 {
                unsafe {
                    (*p_self.offset(i)).bitxor_assign(INV);
                }
            } else {
                let final_inv: u32x4 = get_n_left_mask((self.length % 128) as u8);
                unsafe {
                    (*p_self.offset(i)).bitxor_assign(final_inv);
                }
            }
        }
    }

    // TODO: optimize this (SLOW)
    // returns how many more true values are in self
    // relative to other
    fn __sub__(&self, other: &BinaryArray) -> i32 {
        self.get_list()
            .iter()
            .zip(other.get_list().iter())
            .map(|(x, y)| ((*x as i8) - (*y as i8)) as i32)
            .collect::<Vec<i32>>()
            .into_iter()
            .sum()
    }

    fn __lt__(&self, other: &BinaryArray) -> bool {
        self.__sub__(other) < 0
    }

    fn __gt__(&self, other: &BinaryArray) -> bool {
        self.__sub__(other) > 0
    }

    fn __le__(&self, other: &BinaryArray) -> bool {
        self.__sub__(other) < 0
    }

    fn __ge__(&self, other: &BinaryArray) -> bool {
        self.__sub__(other) > 0
    }

    fn find_first_zero(&self) -> i32 {
        // simpler implementation that doesn't use SIMD
        // for (i, x) in self.binary_storage.iter().enumerate() {
        //     if *x != u32::MAX {
        //         for j in (0..32) {
        //             if (x >> j) & 1 == 0 && (i * 32 + j) < self.length {
        //                 return (i * 32 + j) as i32;
        //             }
        //         }
        //     }
        // }
        // -1i32
        let chunks: isize = (self.binary_storage.len() / 4) as isize;

        let p_self: *const u8x16 = self.binary_storage.as_ptr() as *const u8x16;
        const INV: u8x16 = u8x16::from_array([u8::MAX; 16]);

        let mut _rval: i32 = -1;
        for i in 0..chunks {
            unsafe {
                if *p_self.offset(i) != INV {
                    let c = (*p_self.offset(i)).to_array();
                    for (off, x) in c.iter().enumerate() {
                        if *x != u8::MAX {
                            for j in (0..8).rev() {
                                _rval = (i * 128 + off as isize * 8 + (7 - j)) as i32;
                                if (*x >> j) & 1 == 0 && _rval < self.length as i32 {
                                    return _rval;
                                }
                            }
                        }
                    }
                }
            }
        }
        -1i32
    }

    fn count_ones(&self) -> u32 {
        let mut count: u32 = 0;
        for b in self.binary_storage.iter() {
            count += preload::ONE_COUNT_8_BIT[((*b) >> 24 & preload::BOTTOM_BYTE) as usize];
            count += preload::ONE_COUNT_8_BIT[((*b) >> 16 & preload::BOTTOM_BYTE) as usize];
            count += preload::ONE_COUNT_8_BIT[((*b) >> 8 & preload::BOTTOM_BYTE) as usize];
            count += preload::ONE_COUNT_8_BIT[(*b & preload::BOTTOM_BYTE) as usize];
        }
        count
    }

    fn __len__(&self) -> usize {
        self.length
    }
}

fn compress_bin(v: &Vec<u32>) -> Vec<u32> {
    // store data in blocks of 4 32 bit integers so they can be easily accessed with simd
    let mut bin_arr: Vec<u32> = vec![0u32; (v.len() / 32) + (4 - ((v.len() / 32) % 4))];
    for (i, b) in v.iter().enumerate() {
        bin_arr[i / 32] = ((*b as u32) << (i as u32 % 32u32)) | bin_arr[i / 32];
    }
    bin_arr
}

// a function to return a simd vector masking the leftmost n bits
// of the binary array according to binary array standards
fn get_n_left_mask(nbits: u8) -> u32x4 {
    let mut arr = [0u32; 4];
    let mut i = nbits;
    while i > 0 {
        if i / 32 > 0 {
            arr[((nbits / 32) - i / 32) as usize] = !arr[((nbits / 32) - i / 32) as usize];
            i -= 32u8;
        } else {
            arr[(nbits / 32) as usize] = (arr[(nbits / 32) as usize] << 1) + 1u32;
            i -= 1u8;
        }
    }
    u32x4::from_array(arr)
}

/// A Python module implemented in Rust.
#[pymodule]
fn pynary(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<BinaryArray>()?;
    Ok(())
}
