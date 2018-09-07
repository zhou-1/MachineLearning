# Chapter 1    
从数据中产生model 的算法。 
<br>
<br>
基本术语      
离散值，classification; 连续值，regression.    
Clustering 聚类，将训练集中的目标分为若干组，每一组称为cluster.    
根据训练数据是否有标记信息，分为supervised learning和unsupervised learning.    
学的模型适用于新样本的能力，称为generalization 泛化能力。    
<br>
<br>
假设空间   
归纳 induction 是从特殊到一般的泛化 generalization 过程，从具体的事实归结出一般性规律；    
演绎 deduction 从一般到特殊的特化 specialization 过程，从基础原理推演出具体状况。     
概念学习，最基本是boolean 概念学习，是或则不是。    
学习过程，在所有假设组成的空间中进行搜索的过程，搜索目标是找到与训练集匹配的假设。     
存在着一个与训练集一致的假设集合，称之为版本空间，version space.    
<br>
<br>
归纳偏好    
机器学习算法在学习过程中对某种类型假设的偏好，成为inductive bias. 任何一个有效的机器学习算法必有其归纳偏好。      
可以看作学习算法自身在一个可能很庞大的假设空间中对假设进行选择的启发式或“价值观”。一般性的原则来引导算法确立“正确的”偏好，<b>奥卡姆剃刀(Occam's razor)</b> 是一种最基本的原则，即“若有多个假设和观察一致，就选最简单的那个”。

