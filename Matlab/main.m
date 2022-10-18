
clear all

%initial conditions for state variables
    
    % Electrophysiology (41 variables):
    X0=[-87 7 7 145 145 1.0e-4 1.0e-4 1.2 1.2 0 1 1 1 1 1 0 1 1 0 1 1 0 ...
        1 1 0 1 1 1 1 1 0 1 1 0 0 0 0 1 0 0 0]';
    % X0=[v nai nass ki kss cai cass cansr cajsr m hf hs j hsp jp mL hL hLp a ...
    %     iF iS ap iFp iSp d ff fs fcaf fcas jca nca ffp fcafp xrf xrs xs1 xs2 xk1...
    %     Jrelnp Jrelp CaMKt]';
    %+Mechanical 
    X0(42:48)=[0; 0; 0; 1; 0; 0; 0];
    %X0(42:48)=[XS; XW; CaTrpn; TmB; Zetas; Zetaw; Cd];

%%

CL=1000;%pacing cycle length in ms
beats=200; %1000 / 500
global settings
settings.cell='endo';

options=[];%options for ode solver
tspan=[0 CL]; %[0 CL] variable dt

mech.isacs = 0; % 0 / 1: Isacs
mech.emcoupling = 1; % 0: ORd only; 1: ORd-Land interaction and feedback
    mech.mode = 'intact'; % 'skinned'/'intact'
    mech.lambda = 1; %1.1 max in Isacs; default Land: 1
    mech.dLambda = 0;
mech.calib = 1; %1: Margara calibration in ORd_dutta (approx to ORdmm)

model=@model_ORdmmD_Land; 

for n=1:beats

    [time X]=ode15s(@(t,y)model(t,y,mech,1),tspan,X0);
    X0=X(size(X,1),:);
    n %output beat number to the screen to monitor runtime progress

end

%rename values in the state variables vector
v=X(:,1);       
nai=X(:,2);
nass=X(:,3);
ki=X(:,4);
kss=X(:,5);
cai=X(:,6);     
cass=X(:,7);
cansr=X(:,8);
cajsr=X(:,9);
m=X(:,10);
hf=X(:,11);
hs=X(:,12);
j=X(:,13);
hsp=X(:,14);
jp=X(:,15);
mL=X(:,16);
hL=X(:,17);
hLp=X(:,18);
a=X(:,19);
iF=X(:,20);
iS=X(:,21);
ap=X(:,22);
iFp=X(:,23);
iSp=X(:,24);
d=X(:,25);
ff=X(:,26);
fs=X(:,27);
fcaf=X(:,28);
fcas=X(:,29);
jca=X(:,30);
nca=X(:,31);
ffp=X(:,32);
fcafp=X(:,33);
xrf=X(:,34);
xrs=X(:,35);
xs1=X(:,36);
xs2=X(:,37);
xk1=X(:,38);
Jrelnp=X(:,39);
Jrelp=X(:,40);
CaMKt=X(:,41);
%--------------mechanic model
XS=X(:,42);         
XW=X(:,43);
CaTrpn=X(:,44);
TmB=X(:,45);
Zetas=X(:,46);
Zetaw=X(:,47);
Cd=X(:,48);


%%
%calculate and name dependent variables for the final beat in the
%simulation (i.e. currents and fluxes)
for i=[1:size(X,1)]
    IsJs=model(time(i),X(i,:),mech,0);
    tension=model(time(i),X(i,:),mech,2);
%     INa(i)=IsJs(1);
%     INaL(i)=IsJs(2);
%     Ito(i)=IsJs(3);
%     ICaL(i)=IsJs(4);
%     IKr(i)=IsJs(5);
%     IKs(i)=IsJs(6);
%     IK1(i)=IsJs(7);
%     INaCa_i(i)=IsJs(8);
%     INaCa_ss(i)=IsJs(9);
%     INaK(i)=IsJs(10);
%     IKb(i)=IsJs(11);
%     INab(i)=IsJs(12);
%     ICab(i)=IsJs(13);
%     IpCa(i)=IsJs(14);
%     Jdiff(i)=IsJs(15);
%     JdiffNa(i)=IsJs(16);
%     JdiffK(i)=IsJs(17);
%     Jup(i)=IsJs(18);
%     Jleak(i)=IsJs(19);
%     Jtr(i)=IsJs(20);
%     Jrel(i)=IsJs(21);
%     CaMKa(i)=IsJs(22);
%     Istim(i)=IsJs(23);
%     Isac_P_ns(i)=IsJs(24);
%     Isac_P_k(i)=IsJs(25);
    
    Ttot(i)=tension(1);
    Ta(i)=tension(2);
    Tp(i)=tension(3);
end
%%
figure(101), 
subplot(131),plot(time,v), title('AP'),hold on
subplot(132),plot(time,cai), title('Cai (mM)'),hold on
subplot(133),plot(time,Ta), title('Ta (kPa)'),hold on

