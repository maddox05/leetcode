/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let total=0;
    let roman = {
        I: 1,
        V: 5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000,
    }
 for(let i=s.length-1; i>=0; i--){
    if(roman[s[i]] > roman[s[i-1]]){
        total += roman[s[i]] - roman[s[i-1]]
        i=i-1;
    }
    else{
        total += roman[s[i]]
    }
 }
 return total;
};
