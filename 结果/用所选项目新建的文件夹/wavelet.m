y1 = transpose(Untitled);
[c,l] = wavedec(y1, 10, 'db5');
aq10 = wrcoef('a',c,l,'db5',10);
aq9 = wrcoef('a',c,l,'db5',9);
aq8 = wrcoef('a',c,l,'db5',8);
aq7 = wrcoef('a',c,l,'db5',7);
aq6 = wrcoef('a',c,l,'db5',6);
aq5 = wrcoef('a',c,l,'db5',5);
aq4 = wrcoef('a',c,l,'db5',4);
aq3 = wrcoef('a',c,l,'db5',3);
aq2 = wrcoef('a',c,l,'db5',2);
aq1 = wrcoef('a',c,l,'db5',1);

d10 = wrcoef('d',c,l,'db5',10);
d9 = wrcoef('d',c,l,'db5',9);
d8 = wrcoef('d',c,l,'db5',8);
d7 = wrcoef('d',c,l,'db5',7);
d6 = wrcoef('d',c,l,'db5',6);
d5 = wrcoef('d',c,l,'db5',5);
d4 = wrcoef('d',c,l,'db5',4);
d3 = wrcoef('d',c,l,'db5',3);
d2 = wrcoef('d',c,l,'db5',2);
d1 = wrcoef('d',c,l,'db5',1);

figure
subplot(4,1,1);
plot(y1,'color','k','LineWidth',1.5);
set(gca,'color','w');
axis tight;
xlabel('2015-9-11 到 2016-3-15/15分钟','fontsize',11);
ylabel('用电总量/KWH','fontsize',11);
title('(a)','fontsize',11);
grid on;
subplot(4,1,2);
plot(d5,'color','k','LineWidth',2.0);
axis tight;
xlabel('2015-9-11 到 2016-3-15/15分钟','fontsize',11);
ylabel('每15分钟用电总量波动/15分钟','fontsize',11);
title('(b)','fontsize',11);grid on;
subplot(4,1,3);
plot(d8,'color','k','LineWidth',3.5);
axis tight;
xlabel('2015-9-11 到 2016-3-15/15分钟','fontsize',11);
ylabel('每15分钟用电总量高低峰/15分钟','fontsize',11);
title('(c)','fonsize',11);grid on;
subplot(4,1,4);
plot(a10,'color','k','LineWidth',3.5);
axis tight;
xlabel('2015-9-11 到 2016-3-15/15分钟','fontsize',11);
ylabel('月度用电量变化趋势/15分钟','fonsize',11);
title('(d)','fontsize',11);grid on





