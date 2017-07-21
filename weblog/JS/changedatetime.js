function changedatetime(input) {
    var day = input.substring(0,3);
    var month = input.substring(4,7);
    var date = input.substring(8,10);
    var time = input.substring(11,19);
    var year = input.substring(20);
    
    year = parseInt(year);
    date = parseInt(date);

    var miladi = {
        1 : ['Mar', 21, 31, 'فروردین'],
        2 : ['Apr', 21, 31, 'اردیبهشت'],
        3 : ['May', 22, 31, 'خرداد'],
        4 : ['Jun', 22, 31, 'تیر'],
        5 : ['Jul', 23, 31, 'مرداد'],
        6 : ['Agu', 23, 31, 'شهریور'],
        7 : ['Sep', 23, 30, 'مهر'],
        8 : ['Oct', 23, 30, 'آبان'],
        9 : ['Nov', 22, 30, 'آذر'],
        10 : ['Dec', 22, 30, 'دی'],
        11 : ['Jan', 21, 30, 'بهمن'],
        12 : ['Feb', 20, 29, 'اسفند'],
    };
 
    var year_sh = year-621;
    
    for(var i in miladi){
        mon = miladi[i]
        if(mon[0]==month){
            
            if(i==11 || i==12) {
            year_sh -= 1;
            }
            if(year%4==0){
                miladi[1][1] = 20;
            }
            if(year_sh%4==3){
                miladi[12][1] = 30;
            }
            var equal = miladi[i];
            if (date>=equal[1]){
                var month_sh = equal[3];
                var date_sh = date-equal[1]+1;
            } else {
                var j = i-1;
                if (j==0){
                    j = 12;
                }
                var month_sh = miladi[j][3];
                var date_sh = miladi[j][2]-miladi[i][1]+1+date;
            }
            //console.log(month_sh+'*');
            //console.log(date_sh+'*');
            //console.log(year_sh+'*');
        }
    }
    /*console.log(day+'*');
    console.log(month+'*');
    console.log(date+'*');
    console.log(time+'*');
    console.log(year+'*');*/
    return date_sh + " " + month_sh + " " + year_sh;
}
//console.log(changedatetime('Thu May  4 01:15:07 2017'));