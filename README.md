# post-delay-work-py
Just a simple pyscript for delivery message about being late to your employer.   
**You need pass a parameter** to script in console:   
`python3 post-delay-work.py 999`

Btw, I have this script on my VPS, and rum him from my phone in Termux: `delay 999`. For this you need to do alias in yr Termux:   
`vim ~/.bashrc`   
`alias delay='ssh user@127.0.0.1 python3 scripts/post-delay-work.py' # <=paste
