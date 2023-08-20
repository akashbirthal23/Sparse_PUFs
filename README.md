# Sparse_PUFs
 Melbo wants to design a super-simple PUF that nevertheless offers good security. The idea makes use of a conditional delay unit (CDU). A CDU takes in two inputs, a select bit and a signal. If the select bit is 0, then the CDU relays the input signal to its output without any delay i.e. 0 delay. If the select bit is 1, then the CDU relays the input signal to its output after a delay of p microseconds where p is kept secret and given a certain value of p, it is difficult to create another CDU with that exact value of delay.  CDU PUF: Melbo’s idea is to create a good PUF by stringing together several CDUs in sequence. The select bits to these CDUs becomes the challenge and the responses is the total delay incurred, expressed in microseconds. fig: A PUF created by stringing together 4 CDUs. The response is the total delay incurred in the entire chain. For the challenge 0011, the delay would be p2 + p3 while for the challenge 1010, the delay would be p0 + p2 and for the challenge 1101, the delay would be p0 + p1 + p3.  Sparse CDU PUF: Melbo was happy with this PUF construction till Melbo’s sibling Melbi pointed out that a linear model can easily break this PUF as the responses are simply the sum of the delays of the CDUs chosen by the challenge. To make the PUF more challenging, Melbo devised a clever solution of introducing dummy/irrelevant CDUs into the pipeline. See the figure below that explains the trick. Melbo introduces D CDUs but only S < D of them actually participate in the response generation process. The rest D − S CDUs are disconnected from the chain. Thus, the value of the select bit sent to disconnected CDUs has no effect on the response. To make the problem challenging, Melbo refuses to reveal which S CDUs are active.  Figure 3: A Sparse CDU PUF with D = 7 CDUs out of which only S = 4 CDUs are actually participating in the response generation process. Thus, the values of c1, c3, c4 have no effect on the response. For the challenge 1101011, the delay would be p0 + p5 + p6 and the same delay would be obtained even for the challenge 1000111. For the challenge 0111010, the delay would be p2 + p5 and the same delay would be obtained even for the challenge 0110110.
