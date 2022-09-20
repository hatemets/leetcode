/**
 * @param {string} str
 * @return {boolean}
 */

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:
//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.


const dict = {
    "[": "]",
    "( ": ")",
    "{": "}"
}

const isValid = str => {
    const arr = str.split("")
    const parentheses = Object.entries(dict)

    // Must be of even length
    if (arr.length % 2 !== 0) {
        return false
    }

    while (arr.length > 0) {
        // const [leftPair, rightPair] = [parentheses.find(p => p[0] === arr[0]), parentheses.find(p => p[1] === arr[arr.length - 1])] 
        // console.log(leftPair, rightPair)

        const x = parentheses.find(p => p[0].toString() == arr[0].toString())

        // if (leftPair === undefined || rightPair === undefined) {
        //     console.log("tra")
        //     return 9999
        // }
        // if (leftPair[0] !== rightPair[0]) {
        //     return false
        // }
        // else {
        //     // Remove the first and last element
        //     arr.splice(0, 1)
        //     arr.splice(arr.length - 1, 1)
        // }
    }

    return true
}

console.log(isValid("()"))
