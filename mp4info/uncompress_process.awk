#! /bin/bash

BEGIN{
    FS="[ \t+]"

    uncompress_ct=sprintf("./data/uncompress_ct_beta_%s", date)
    uncompress_fail_ratio=sprintf("./data/uncompress_fail_day_beta")
    
    system("rm -rf " uncompress_ct)

    fail_beta=0
    total_beta=1
}

{
    ver=$6
    if(index(ver, "3.0.0")){
        if($12==1){
            print $11 >> uncompress_ct
        }else{
            fail_beta+=1
        }
        total_beta+=1
    }
}

END{
    print date, total_beta, fail_beta >> uncompress_fail_ratio
}
