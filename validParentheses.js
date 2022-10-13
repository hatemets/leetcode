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
    str = str.split('').map(el => el.trim())
    const len = str.length
    let left = []

    const keys = Object.keys(dict).map(el => el.trim())
    const entries = Object.entries(dict)

    for (let i = 0; i < len; ++i) {
        if (i === 0 || keys.includes(str[i])) {
            left.push(str[i])
        }
        else if (left.length > 0) {
            const found = entries.find(pair => pair[0].trim() === left[left.length - 1])

            if (found === undefined || found[1] !== str[i]) {
                return false
            }
            else {
                left.pop()
            }
        }
        else {
            return false
        }
    }

    return left.length === 0
}

console.log(isValid("()"))
console.log(isValid("(())"))
console.log(isValid("((()))"))
console.log(isValid("[()]"))
console.log(isValid("({[]})"))
console.log(isValid("({}[[()]])"))
console.log(isValid("()"))
console.log(isValid("(]"))
