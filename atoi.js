const atoi = str => {
    str = str.trim().split("").filter(el => typeof Number(el) === "number")
    console.log(str)

    let isPositive = true

    if (["+", "-"].includes(str[0])) {
        if (str[0] === "-") {
            isPositive = false
        }

        str.splice(0, 1)
    }

    str = str.reduce((a, b) => a + b)
    let result = Number(str) * (!isPositive ? -1 : 1)

    if (result > Math.pow(2, 31) - 1) {
        result = Math.pow(2, 31) - 1
    }
    else if (result < -Math.pow(2, 31)) {
        result = -Math.pow(2, 31)
    }

    return result
}

console.log(atoi("532532 with words"))
