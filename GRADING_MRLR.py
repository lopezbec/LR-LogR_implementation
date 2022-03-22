def GRADING(X_norm_sklearn,X_norm,theta_best,theta_cost,MAE_val,MAE_skl,MSE_val,MSE_skl,RMSE_val,RMSE_skl,R_square_val,R_square_skl,RMSE_training_LR,RMSE_test_LR,ridge_regression_pipeline,RMSE_training_Ridge,RMSE_test_Ridge,RMSE_training_Lasso,RMSE_test_Lasso,lasso_regression_pipeline,coef_sogmax):


    grades={"feature_Normalize_implementation":False, 
             "MAE":False,
            "MSE":False,"RMSE":False,
            "R_square":False,"Ridge_LR_working":False,"Lasso_LR_working":False, 
            "Softmax_X_train":False}




    try:
        if(round(X_norm_sklearn[1,1],3)==-0.226): grades["feature_Normalize_implementation"]=True
    except: grades["feature_Normalize_implementation"]=False

    try:
        if(round(MAE_val,5)==round(MAE_skl,5)): grades["MAE"]=True
    except: grades["MAE"]=False
    
    try:
        if(round(MSE_val,5)==round(MSE_skl,5)): grades["MSE"]=True
    except: grades["MSE"]=False

    try:
        if(round(RMSE_val,5)==round(RMSE_skl,5)): grades["RMSE"]=True
    except: grades["RMSE"]=False

    try:
        if(round(R_square_val,5)==round(R_square_skl,5)): grades["R_square"]=True
    except: grades["R_square"]=False

    try:
        if(RMSE_training_Ridge!=None and RMSE_test_Ridge!=None): grades["Ridge_LR_working"]=True
    except: grades["Ridge_LR_working"]=False

    try:
        if(RMSE_training_Lasso!=None and RMSE_test_Lasso!=None): grades["Lasso_LR_working"]=True
    except: grades["Lasso_LR_working"]=False

    try:
        if(round(coef_sogmax[0,0],2)==-2.5): grades["Softmax_X_train"]=True
    except: grades["Softmax_X_train"]=False


    for x in grades:
        print (x,':',grades[x])
        
    print(" ")
    print("RMSE from Training=" + str(round(RMSE_training_LR, 5)))
    print("RMSE Ridge LR from Training=" + str(round(RMSE_training_Ridge,4)))
    print("RMSE Lasso LR from Training=" + str(round(RMSE_training_Lasso,4)))
    print(" ")
    print("RMSE from Test=" + str(round(RMSE_test_LR,4)))
    print("RMSE Ridge LR from Test=" + str(round(RMSE_test_Ridge,4)))
    print("RMSE Lasso LR from Test=" + str(round(RMSE_test_Lasso,4)))
    print(" ")
    print("NORMALIZED???")
    print(" ")
    print(ridge_regression_pipeline.named_steps)
    print(" ")
    print(lasso_regression_pipeline.named_steps)
    print("Check Wine 0.3 training, X_trainng + X_test?")
