PERIODIC_ELEMENTS = """
h,he,li,be,b,c,n,o,f,ne,na,mg,al,si,p,s,cl,ar,k,ca,sc,ti,v,cr,mn,fe,co,ni,cu,zn,ga,ge,as,se,br,kr,
rb,sr,y,zr,nb,mo,tc,ru,rh,pd,ag,cd,in,sn,sb,te,i,xe,cs,ba,la,ce,pr,nd,pm,sm,eu,gd,tb,dy,ho,er,tm,
yb,lu,hf,ta,w,re,os,ir,pt,au,hg,tl,pb,bi,po,at,rn,fr,ra,ac,th,pa,u,np,pu,am,cm,bk,cf,es,fm,md,no,
lr,rf,db,sg,bh,hs,mt,ds,rg,cn,nh,fl,mc,lv,ts,og""".replace('\n', '').split(',')


def is_periodic(word):
    if len(word) == 0:
        return True
    result = False
    if word[0] in PERIODIC_ELEMENTS:
        result = is_periodic(word[1:])
    if not result and word[:2] in PERIODIC_ELEMENTS:
        result = is_periodic(word[2:])
    return result


def main():
    longest = None
    with open('american-english-insane') as words:
        for line in words:
            word = line.lower().strip()
            if longest is None or len(word) > len(longest) and is_periodic(word):
                longest = word
    print(longest)


if __name__ == '__main__':
    main()
