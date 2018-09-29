# An Application Of Supervised Learning : Autonomous Deriving, ALVINN      
Starts now, learning from http://www.holehouse.org/mlclass/     
http://www.holehouse.org/mlclass/01_02_Introduction_regression_analysis_and_gr.html    

<b> Linear Regression </b>       
Take training set, Pass into a learning algorithm, Algorithm outputs a function (denoted h ) (h = hypothesis)     
present h as: hθ(x) = θ0 + θ1x. Means Y is a linear function of x! θi are parameters; θ0 is zero condition; θ1 is gradient          
This kind of function is a linear regression with one variable, Also called univariate linear regression    
Summary: A hypothesis takes in some variable; Uses parameters determined by a learning system; Outputs a prediction based on that input     

<b> Linear regression - implementation (cost function) </b>     
A cost function lets us figure out how to fit the best straight line to our data.       
Choosing values for θi (parameters), Based on our training set we want to generate parameters which make the straight line, want to solve a minimization problem - Minimize (hθ(x) - y)2, Sum this over the training set.  
want to minimize this cost function.       
Hypothesis - is like your prediction machine, throw in an x value, get a putative y value      
Cost - is a way to, using your training data, determine values for your θ values which make the hypothesis as accurate as possible      

<b> Deep look at cost function </b>    
why we want to use cost function?    
The cost function determines parameters; The value associated with the parameters determines how your hypothesis behaves, with different values generate different       
simplified cost function     
visual the redult, Instead of a surface plot we can use a contour figures/plots     

<b> Gradient descent algorithm 梯度下降 </b>    
Minimize cost function J, Used all over machine learning for minimization    
We have J(θ0, θ1), We want to get min J(θ0, θ1)     
Gradient descent applies to more general functions J(θ0, θ1, θ2 .... θn), min J(θ0, θ1, θ2 .... θn)      
Start with initial guesses    
Start at 0,0 (or any other value)    
Keeping changing θ0 and θ1 a little bit to try and reduce J(θ0,θ1)    
Each time you change the parameters, you select the gradient which reduces J(θ0,θ1) the most possible     
Repeat    
Do so until you converge to a local minimum    
Has an interesting property      
<b> Two key terms in the algorithm </b>     
Alpha   
Derivative term    
<b> When you get to a local minimum </b>    
Gradient of tangent/derivative is 0    
So derivative term = 0    
alpha * 0 = 0    
So θ1 = θ1- 0    
So θ1 remains the same    


<b> Linear regression with gradient descent </b>   











