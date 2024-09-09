impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
    let mut odd: i32 = 0;
    let mut even: i32 = 0;
    for (index, pile) in piles.iter().enumerate() {
        if(index % 2 == 0){
            even+= pile;
        }
        else{
            odd+= pile;
        }
    }
    if(even!=odd){
        return true;
    }
    return false;
}

}
