[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>The actual mean number of kids is `0.820618884735`, while the biased mean number of kids is `2.39666537418`. The distribution for actual number of kids vs. biased number of kids can be seen in the bar graph below:



>>For this exercise, I chose not to use Downey's pre-defind Histograpm and PMF classes, as I couldn't follow in his code creating them very well. Instead, I wrote my own functiosn to create histograms and PMF's as dictionary opjects. See below:

				#ThinkStats Exercise 3-1 (The Class Size Paradox & Biased Distributions)

				import thinkstats2
				import pandas as pd
				import copy as cp
				from matplotlib import pyplot as pp

				##Read In Respondent-Level Data for Both Males and Females (adapt Downey's Preganncy data read-in for new datasets)
				def ReadData (dct_file, dat_file):
				    dct = thinkstats2.ReadStataDct(dct_file)
				    df = dct.ReadFixedWidth(dat_file, compression='gzip')
				    return df

				male_resp=ReadData("2002Male.dct","2002Male.dat.gz")
				fem_resp=ReadData("2002FemResp.dct","2002FemResp.dat.gz")


				##Concatenate Male & Female Respondent Data Frames
				all_resp=pd.concat([male_resp,fem_resp], ignore_index=True)


				##Produce PMF
				def ProduceHist(s): #input is a Pandas series
					d={}

					for i in range(0,len(s)):
						d[s[i]]=d.get(s[i],0)+1

					return d

				def ProducePMF(s):
					d=ProduceHist(s)
					for key in d:
						d[key]=float(d[key])/len(s)
				 
					return d

				num_kids_hist=ProduceHist(all_resp["numkdhh"])
				num_kids_pmf=ProducePMF(all_resp["numkdhh"])


				#Produce biased PMF - multiply each PMF dictionary value by it's corresponding key, then normalize. 
				def ProduceBiasedPMF(d):
					new_d=cp.copy(d)
					total=0

					#Multiply by Key value (# kids/ household)
					for k in new_d:
						new_d[k]=new_d[k]*k
						total +=new_d[k]

					#Normalize PMF
					for k in new_d:
						new_d[k]=new_d[k]/ total

					return new_d

				num_kids_pmf_biased=ProduceBiasedPMF(num_kids_pmf)

				print "Histogram:", num_kids_hist
				print "Actual PMF:", num_kids_pmf
				print "Biased PMF:", num_kids_pmf_biased

				#Compute mean for actual and biased distributions
				def ComputeMean(d):
					avg=0

					for k in d:
						avg +=k*d[k]

					return avg

				print "Actual Mean Number of Kids", ComputeMean(num_kids_pmf)
				print "Biased Mean Number of Kids", ComputeMean(num_kids_pmf_biased)


				#Graph using Matplotlib
				width=0.5

				ticks_1=num_kids_pmf.keys()
				ticks_2=[]
				for t in ticks_1:
					ticks_2.append(t+width)

				bar1=pp.bar(ticks_1, num_kids_pmf.values(), width, color="b")
				bar2=pp.bar(ticks_2, num_kids_pmf_biased.values(), width, color="g")
				pp.title("Actual vs. Biased Number of Kids per Household Distributions")
				pp.xlabel("Number of Children per Household")
				pp.ylabel("Probability")
				pp.legend((bar1[0], bar2[0]), ("Actual", "Biased"))
				pp.show()
