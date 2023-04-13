/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
};

/* EXTRA MEMORY = 1 NEW ARRAY, O(N)
var isValid = function(s) {
    let stack = []
    for (let i=0;i<s.length;i++) {
      if (s[i] == '(') {
        stack.push(1)
      }
      else if (s[i] == '{') {
        stack.push(2)
      }
      else if (s[i] == '[') {
        stack.push(3)
      }
      else {
        let top = stack.pop()
        if (s[i] == ')' && top != '1') {
          return false
        }
        else if (s[i] == '}' && top != '2') {
          return false
        }
        else if (s[i] == ']' && top != '3') {
          return false
        }
      }
    }
    return true
};
 */
