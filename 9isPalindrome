/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

};

/* O(N/2)
var isPalindrome = function(s) {
    s = s.replace(/[^a-zA-Z]/g, "").toLowerCase()
    console.log(s)
    for (let i=0;i<(s.length/2);i++) {
        console.log("testing",s[i], "and", s[s.length-1-i])
        if (s[i] != s[s.length-i-1]) {
            console.log("error!",i,s.length-i-1)
            console.log(s[i], "and", s[s.length-i-1])
            return false
        }
    }
    return true
};
 */
/* EXTRA MEMORY, O(N/2)
    r = ""
    s = s.replace(/[^a-zA-Z]/g, "").toLowerCase()
    if(s.length%2 == 0) {
        for (let i=0;i<(s.length/2);i++) {
            r = r + s[s.length-1-i]
        }
        s = s.substring(0,(s.length/2))
        if (r === s) return true
    }
    else {
        for (let i=0;i<(s.length/2) - 1;i++) {
            r = r + s[s.length-1-i]
        }
        s = s.substring(0,(s.length/2))
        if (r === s) return true
    }
    return false
 */
