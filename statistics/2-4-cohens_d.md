[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>Cohen's d for total baby weight between first borns and other babies is `-0.0886729270726`. The negative sign on Cohen's d indicates that first born children, on average, weigh less than their later siblings. However, the relatively small size of Cohen's d indicates this difference is slight - less than 1/10th of a standard deviation. Cohen's d for pregnacy length is `-0.0313117858337`. As such, the effect size for differency in pregnancy length is even smaller than the effect for weight - less that 1/20th of a standard deviation 

>>I used Downey's Cohen's d function to calculate Cohen's d for the NSFG data. The code I used was:
```
from nsfg import ReadFemPreg
from thinkstats2 import CohenEffectSize

"""Read NDFG Data into Panda's Data Frame"""
nsfg=ReadFemPreg() #Read NSFG Data into Pandas Data Frame

"""2-4) Compute Cohen's d for Infant Weight among First/ Later Births"""
first=nsfg[(nsfg.outcome==1) & (nsfg.birthord==1)]["totalwgt_lb"]
other=nsfg[(nsfg.outcome==1) & (nsfg.birthord>1)]["totalwgt_lb"]

print "First baby mean weight", first.mean()
print "Other baby mean weight", other.mean()
print "Difference", first.mean()-other.mean()
print "Cohen's D for Infant Weight for First/ Later Babies:", CohenEffectSize(first, other)

"""Compute Cohen's d for length of pregnancy"""
first=nsfg[nsfg.pregordr==1]["prglngth"]
other=nsfg[nsfg.pregordr>1]["prglngth"]

print "First baby mean preg length", first.mean()
print "Other baby mean preg length", other.mean()
print "Diference", first.mean()-other.mean()
print "Cohen's D for Preg Length for First/ Later Babies", CohenEffectSize(first, other)
```
