#! /bin/bash

BEGIN{
    FS="[ \t+]"

    #output file
    info_cost_time=sprintf("./data/mp4info_ct_beta_%s", date)
    task_size=sprintf("./data/task_size_beta_%s", date)
    
    ratio_hour_beta=sprintf("./data/info_ratio_hour_beta_%s", date)
    ratio_day_beta=sprintf("./data/info_ratio_day_beta")

    system("rm -rf " info_cost_time)
    system("rm -rf " task_size)
    system("rm -rf " ratio_hour_beta)

    for(i=0;i<24;i++){
        fail_beta[i]=0
        total_beta[i]=1
    }

    fail_sum_beta=0
    total_sum_beta=1
}

{
    time=$3
    hour=(int(time/3600)+8)%24
    ver=$6    

    if(index($0, "like")){
        next
    }
    if(index(ver, "3.0.0")){
        if($13==0){
            fail_beta[hour]+=1
            fail_sum_beta+=1
        }        

        total_beta[hour]+=1
        total_sum_beta+=1   

        #cost time
        print $13, $12 >> info_cost_time
        if($13==1 && $10!="NaN"){
            print $10, $11 >> task_size     
        }
    }
}

END{
    for(i=0;i<24;i++){
        print i, total_beta[i], fail_beta[i] >> ratio_hour_beta
    }

    print date, total_sum_beta, fail_sum_beta >> ratio_day_beta
}


