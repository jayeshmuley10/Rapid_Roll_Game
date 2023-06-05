import shelve
highscore=2
d = shelve.open('score.txt')    
d['score1'] =0
d['score2'] = 0
d['score3'] = 0
d['score4'] = 0
d['score5'] = 0
d['xp']=0
print('done')
d.close()








 
 
            


