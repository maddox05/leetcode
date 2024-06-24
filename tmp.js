function check_to_arrays(arr1,arr2){
    for(let i=0; i<arr1.length; i++){
        if(arr1[i]===arr2[i]){
        }
        else{
            return false;
        }
    }
    return true;
}

function check_if_r_is_right(arr, index){
    for(let i=index; i<arr.length; i++){
        if(arr?.[i+1]==='R'){
            return i+1;
        }
    }
    return -1;
}

function check_if_l_is_left(arr, index){
    try{
        for(let i=index; i>=0; i--){
        if(arr?.[i-1]==='L'){
            return i-1;
        }
        }
        return -1;
    }
    catch(error){
        console.log(error)
    }
    
}

/**
 * @param {string} start
 * @param {string} target
 * @return {boolean}
 */
var canChange = function(start, target) {
    start= start.split('')
    target = target.split('')
    let first_r = -1;
    let ls_at_start =0;
    for(let i=0; i<start.length+1; i++){
        //if(start[i] === "_"){}
        if(start[i] === 'L' && start?.[i-1] === '_'){
            let l_loc = check_if_l_is_left(target,i);

            if(l_loc === -1){

            }
            else{
                if(i===ls_at_start){
                ls_at_start++;
            }
            start[i]='_'
            start[l_loc]='L'
            i=ls_at_start;
            }
            
        }
        else if(start[i] === 'R' && start?.[i+1] === '_' && (check_if_r_is_right(target,i))){
            if(first_r === -1){
                first_r = i
            }
            start[i]='_'
            start[i+1]='R'
            i=first_r
        }
    }
    if(check_to_arrays(start,target)){
            return true;
    }
    return false;
    
};
