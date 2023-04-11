/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
};
/* SORTED SOLUTION O(N)
var isAnagram = function(s, t) {
    let sArr = s.split("")
    let tArr = t.split("")
    console.log(sArr.sort())
    console.log(tArr.sort())
    for (let i in sArr) {
        if (sArr[i] != tArr[i]) return false
    }
    return true
};
 */

/*  HASHMAP SOLUTION O(N)
var isAnagram = function(s, t) {
    let sarr = s.split("")
    let tarr = t.split("")
    let first = new Map()
    let second = new Map()

    for (let i = 0; i < sarr.length; i++) {
        if (first.get(sarr[i]) === undefined) {
            first.set(sarr[i],1)
        }
        else {
            first.set(sarr[i],(first.get(sarr[i]) + 1))
        }
        if (second.get(tarr[i]) === undefined) {
            second.set(tarr[i],1)
        }
        else {
            second.set(tarr[i],(second.get(tarr[i]) + 1))
        }
    }
    let returnValue = true
    first.forEach((value, key) => {
        if (second.get(key) != value) {
        returnValue = false
        }
    });
    return returnValue
};
 */

/* BRUTE FORCE, COMPARE EACH CHAR FROM S AND REMOVE THAT CHAR FROM T O(N^2)
var isAnagram = function(s, t) {
    let sArr = s.split("")
    let tArr = t.split("")
    if (sArr.length != tArr.length) {
        return false
    }
    for (let i = 0; i < sArr.length; i++) {
        for (let j = 0; j < tArr.length; j++) {
            if (sArr[i] === tArr[j]) {
                tArr.splice(j,1)
                continue
            }
        }
    }
    if (tArr.length == 0) {
        return true
    } return false
};
 */
