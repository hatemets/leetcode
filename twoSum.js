/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

const twoSum = (arr, target) => {
    const len = arr.length
    for (let i = 0; i < len; ++i) {
        for (let j = i + 1; j < len; ++j) {
            if (arr[i] + arr[j] === target) {
                return [i, j]
            }
        }
    }
}


const nums = [1,2,3,4,5]
const target = 7

console.log(twoSum(nums, target))
