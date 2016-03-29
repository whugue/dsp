[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>The model specified estimates that 34.2% of the male population would be eligible for Blue Mens Group. To determine the percentage of eligible males, I calculated the percentile rank of 5'10" men (i.e. the percent of all men 5'10" and shorter) and the percentile rank of 6'11" men (i.e. the percent of all men 6'1" and shorter). The difference between these two percentile ranks gives the total percent of males who fall within this range.

>>According to the nifty calculator here http://www.thecalculatorsite.com/conversions/common/cm-to-feet-inches.php, I converted the shortest and tallest blue men's heights into centimeters.

>>*5'10" ~177.8cm
>>*6'1" ~185.4cm

>>I think use the following code to estimate the percentage of eligible males:

	import scipy.stats
	shortest=scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)
	tallest=scipy.stats.norm.cdf(185.4, loc=178, scale=7.7)
	diff=tallest-shortest

	print "The Percent of Men 5'10 and shorter is", shortest*100 #~49.0%
	print "The Percent of Men 6'1 and shorter is", tallest*100 #~83.2%
	print "The Percent of Men between 5'10 and 6'1 is", diff*100 #~34.2%
