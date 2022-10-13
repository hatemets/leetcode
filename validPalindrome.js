const util = require("util") 

/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

@param {string} s
@return {boolean}
*/

const isPalindrome = str => {
    // match non-alphanumeric characters and replace them with empty spaces
    str = str.toLowerCase().replace(/[^a-z0-9]/gi, "")
    let [start, end] = [0, str.length - 1]

    while (start < end) {
        if (str[start] !== str[end]) return false
        ++start
        --end
    }

    return true
}

console.log(isPalindrome("nabaxaban"))
console.log(isPalindrome(""))
console.log(isPalindrome("anna"))
console.log(isPalindrome("anuna"))
console.log(isPalindrome("x"))
console.log(isPalindrome("jakaz"))
console.log(isPalindrome("A man, a plan, a canal: Panama"))
