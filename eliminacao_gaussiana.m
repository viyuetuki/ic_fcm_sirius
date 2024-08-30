tic
clc
clear all

fprintf('Sendo a matriz original do problema:\n')
A = [1 2; 3 -1]

b = [3; 1]

n = length(A)

for k = 1:n-1
  for i = k+1:n
    m = A(i,k)/A(k,k);
    b(i)= b(i)-m*b(k);
    A(i,k)=0;
    for j = k+1:n
      A(i,j) = A(i,j)-m*A(k,j);
    endfor
  endfor
endfor

x(n)=b(n)/A(n,n);

for k = (n-1):-1:1
  s = 0;
  for j = (k+1):n
    s = s + A(k,j)*x(j);
    x(k) = (b(k) - s)/ A(k,k);
  endfor
endfor
fprintf('Considerando a matriz escalonada:\n')
A
fprintf('A solução é:\n')
x
toc
