import time
import lattice,fileio
import os,sys

def runparams(param,n_equil=500000,n_calc=250000):
    L = lattice.Lattice(n = param[0],T=param[3],state=param[1],J=param[2])
    print("Run:%s Equilibrating..." % L.config)
    for i in xrange(n_equil):
        L.step()
    print("Done!")

    Etotals = []
    Stotals = []
    Etotal = L.H()
    Stotal = L.spintotal()
    Etotals.append(Etotal)
    Stotals.append(Stotal)

    print("Run:%s Calculating..." % L.config)
    for i in xrange(n_calc):
        Ediff,Sdiff = L.step()
        Etotal += Ediff
        sys.stdout.flush()
        Stotal += Sdiff
        Etotals.append(Etotal)
        Stotals.append(Stotal)

    print("Done!")

    fileio.writedata("results/%s.txt" % L.config,[Etotals,Stotals])

Ts = [5.]#[0.01*(x+1) for x in xrange(0,500)]
ns = [20]
states = [1]
Js = [1.]
params = [(n,state,J,T) for n in ns for state in states for J in Js for T in Ts ]

def profile():
    import profile
    profile.run("run.runparams(run.params[0],200000,100000)")

if __name__ == "__main__":
    t1 = time.time()
    #job_server = pp.Server()
    #for param in params:
    #    job_server.submit(runparams,(param,))
        
    for param in params: runparams(param)
    t2 = time.time()
    dt = t2 - t1

    hrs = int(dt/3600)
    dt -= 3600*hrs
    mins = int(dt/60)
    dt -= 60*mins
    secs = dt
    
    print("Job completed in %d hours, %d minutes and %f seconds" % (hrs,mins,secs))
