import sys, mosek as msk
def dea(data, ninputs, dmu):
	inf = 0.0
	vars = [x for x in data ]
	mx, my, n = ninputs, len(data[dmu]) - ninputs, len(data) + 1
	asub, acof, colcnt = [], [], (n+1)*[0]
	nz, idx = 0, 0
	for v in vars:
		acof += data[v]
		asub += range(mx+my)
		nz += mx+my
		colcnt[idx+1] = nz
		idx += 1
	acof += [ -xi for xi in data[dmu][:ninputs] ]
	asub += range(mx)
	colcnt[idx+1] = colcnt[idx] + mx
	env = msk.Env()
	env.init ()
	task = env.Task(0,0)
	task.set_Stream (msk.streamtype.log, lambda x: sys.stdout.write(x))
	task.inputdata (mx+my, # number of constraints
	n, # number of variables
	(n-1)*[0.0] + [1.0], # linear objective coefficients
	0.0, # objective fixed value
	colcnt[:-1], colcnt[1:],
	asub, acof,
	mx*[ msk.boundkey.up ] + my*[ msk.boundkey.lo ], # bkc
	mx*[-inf] + data[dmu][ninputs:], # blc
	mx*[0] + my*[inf], # buc
	(n-1)*[ msk.boundkey.lo ] + [ msk.boundkey.fr ], # bkx
	(n-1)*[0] + [-inf], # blx
	(n-1)*[inf] + [inf] # bux
	)
	task.putobjsense(msk.objsense.minimize)
	task.optimize()
	x = msk.array.zeros(n, float)
	task.getsolutionslice(msk.soltype.bas, msk.solitem.xx, 0, n, x)
	theta, lam = x[-1], dict()
	for k in range(len(vars)): lam[vars[k]] = x[k]
	return theta, lam
data = {'DMU1': [ 5, 14, 9, 4, 16],
'DMU2': [ 8, 15, 5, 7, 10],
'DMU3': [ 7, 12, 4, 9, 13]}
for dmu in ['DMU1','DMU2','DMU3']:
	theta, lam = dea(data, 2, dmu)
	print "Efficiency for %s : %1.3e" %(dmu, theta)