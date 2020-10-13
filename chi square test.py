from scipy.stats import chi2_contingency 
  
# defining the table 
data = [[262,234,204,190,210], [220,220,220,220,220]] 
stat, p, dof, expected = chi2_contingency(data) 
  
# interpret p-value 
alpha = 0.05
print("p value is " + str(p)) 
if p <= alpha: 
    print('Dependent (reject H0)') 
else: 
    print('Independent (H0 holds true)') 
