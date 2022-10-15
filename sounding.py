# read sounding
import urllib
import matplotlib.pyplot as plt
import numpy as np

def read_sounding(url):
    pressure=[]
    altitude=[]
    temp    =[]
    tdew=[]
    lines  = urllib.request.urlopen(url).readlines()
    for line in lines[10:76]: # 100
        entries = line.decode("utf-8").split()
        if len(entries) == 11: # check that we have 11 columns
            pressure.append(float(entries[0]))
            altitude.append(float(entries[1]))
            temp.append(float(entries[2]))
            tdew.append(float(entries[3]))
    return(pressure,altitude,temp,tdew)

def location(url):
    lines  = urllib.request.urlopen(url).readlines()
    lon=lines[81] # longitude 132
    lat=lines[80] # latitude  131
    lon=float(lon.decode("utf-8").split(":")[1])
    lat=float(lat.decode("utf-8").split(":")[1])
    return(lat,lon)   

if __name__ == '__main__':
    #Santa Domingo (tropics)
    url1     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM=78486'    
    p1,h1,t1,td1   = read_sounding(url1)
    #lat1,lon1 = location(url1)
    
    #Kansas City (Mid)
    url2     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM=72451'    
    #lat2,lon2 = location(url2)
    p2,h2,t2,td2   = read_sounding(url2)
    
    #Cambridge Bay (polar)
    url3     = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2021&MONTH=10&FROM=0512&TO=0512&STNM=71925'    
    p3,h3,t3,td3   = read_sounding(url3)
    #lat3,lon3 = location(url3)
    
    #temp vs altitude plot
    p3,h3,t3,td3   = read_sounding(url3)
    plt.plot(t1,h1,'o--', label='Tropics')
    plt.plot(t2,h2,'o--', label='Mid Latitude')
    plt.plot(t3,h3,'o--', label='Polar')
    plt.xlabel("temperature [C]")
    plt.ylabel("altitude [m]")
    plt.legend()
    plt.show()
    
 
    
#   Santa Domingo

    from scipy import interpolate
    H_new=np.arange(100,20000,100)
    f = interpolate.interp1d(np.array(h1), np.array(t1),fill_value="extrapolate")
    T_new=f(H_new)
    #plt.plot(T_new, H_new,'*r')
    
    
    import metpy.calc as mpcalc
    from metpy.plots import SkewT
    from metpy.units import units
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)

    t1new=t1* units.degC
    td1new=td1* units.degC
    p1new=p1* units.hPa
    

    # Calculate parcel profile
    prof = mpcalc.parcel_profile(p1new, t1new[0], td1new[0]).to('degC')
    u1 = np.linspace(-10, 10, len(p1new)) * units.knots
    v1 = np.linspace(-20, 20, len(p1new)) * units.knots

    skew.plot(p1new, t1new, 'r')
    skew.plot(p1new, td1new, 'g')
    skew.plot(p1new, prof, 'k')  # Plot parcel profile
    skew.plot_barbs(p1new[::2], u1[::2], v1[::2])

    skew.ax.set_xlim(-50, 35)
    skew.ax.set_ylim(1000, 100)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    skew.shade_cape(p1new, t1new,prof)
    skew.shade_cin(p1new, t1new,prof)
    #plt.title('lat='+str(lat1)+' lon='+str(lon1))
    plt.title('Tropics Skew-T Plot')
    plt.show()   
    
    #Kansas City

    H_new=np.arange(100,20000,100)
    f = interpolate.interp1d(np.array(h2), np.array(t2),fill_value="extrapolate")
    T_new=f(H_new)
    #plt.plot(T_new, H_new,'*r')
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)
    t2new=t2* units.degC
    td2new=td2* units.degC
    p2new=p2* units.hPa
    

    # Calculate parcel profile
    prof = mpcalc.parcel_profile(p2new, t2new[0], td2new[0]).to('degC')
    u2 = np.linspace(-10, 10, len(p2new)) * units.knots
    v2 = np.linspace(-20, 20, len(p2new)) * units.knots

    skew.plot(p2new, t2new, 'r')
    skew.plot(p2new, td2new, 'g')
    skew.plot(p2new, prof, 'k')  # Plot parcel profile
    skew.plot_barbs(p2new[::2], u2[::2], v2[::2])

    skew.ax.set_xlim(-50, 35)
    skew.ax.set_ylim(1000, 100)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    skew.shade_cape(p2new, t2new,prof)
    skew.shade_cin(p2new, t2new,prof)
    #plt.title('lat='+str(lat2)+' lon='+str(lon2))
    plt.title('Mid - Latitude Skew-T Plot')
    plt.show()   
    
    
    #Cambridge Bay

    H_new=np.arange(100,20000,100)
    f = interpolate.interp1d(np.array(h3), np.array(t3),fill_value="extrapolate")
    T_new=f(H_new)
    #plt.plot(T_new, H_new,'*r')
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)
    t3new=t3* units.degC
    td3new=td3* units.degC
    p3new=p3* units.hPa
    

    # Calculate parcel profile
    prof = mpcalc.parcel_profile(p3new, t3new[0], td3new[0]).to('degC')
    u3 = np.linspace(-10, 10, len(p2new)) * units.knots
    v3 = np.linspace(-20, 20, len(p2new)) * units.knots

    skew.plot(p3new, t3new, 'r')
    skew.plot(p3new, td3new, 'g')
    skew.plot(p3new, prof, 'k')  # Plot parcel profile
    skew.plot_barbs(p3new[::2], u3[::2], v3[::2])

    skew.ax.set_xlim(-50, 35)
    skew.ax.set_ylim(1000, 100)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()
    skew.shade_cape(p3new, t3new,prof)
    skew.shade_cin(p3new, t3new,prof)
    #plt.title('lat='+str(lat2)+' lon='+str(lon2))
    plt.title('Polar Skew-T Plot')
    plt.show()   
    
    
    
    
   