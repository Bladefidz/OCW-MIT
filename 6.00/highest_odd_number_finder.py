#Finger exercise
#Introducing to Computation and Programming Using Python Spring 2011
#Page 20

print '######################################';
print '#########Highest value finder#########';
print '######################################';
print 'Please enter 10 ODD NUMBER';
print '\n';

one = int(raw_input('Enter 1st number: '));
if one%2 == 1:
    two = int(raw_input('Enter 2nd number: '));
    if two%2 == 0:
        print 'please enter ONLY ODD NUMBER!';
    if two%2 == 1:
        if two >= one:
            MAX = two;
        if two < one:
            MAX = one;
        three = int(raw_input('Enter 3rd number: '));
        if three%2 == 0:
            print 'please enter ONLY ODD NUMBER!';
        if three%2 == 1:
            if three > MAX:
                MAX = three;
            four = int(raw_input('Enter 4th number: '));
            if four%2 == 0:
                print 'please enter ONLY ODD NUMBER!';
            if four%2 == 1:
                if four > MAX:
                    MAX = four;
                five = int(raw_input('Enter 5th number: '));
                if five%2 == 0:
                    print 'please enter ONLY ODD NUMBER!';
                if five%2 == 1:
                    if five > MAX:
                        MAX = five;
                    six = int(raw_input('Enter 6th number: '));
                    if six%2 == 0:
                        print 'please enter ONLY ODD NUMBER!';
                    if six%2 == 1:
                        if six > MAX:
                            MAX = six;
                        seven = int(raw_input('Enter 7th number: '));
                        if seven%2 == 0:
                            print 'please enter ONLY ODD NUMBER!';
                        if seven%2 == 1:
                            if seven > MAX:
                                MAX = seven;
                            eight = int(raw_input('Enter 8th number: '));
                            if eight%2 == 0:
                                print 'please enter ONLY ODD NUMBER!';
                            if eight%2 == 1:
                                if eight > MAX:
                                    MAX = eight;
                                nine = int(raw_input('Enter 9th number: '));
                                if nine%2 == 0:
                                    print 'please enter ONLY ODD NUMBER!';
                                if nine%2 == 1:
                                    if nine > MAX:
                                        MAX = nine;
                                    ten = int(raw_input('Enter 10th number: '));
                                    if ten%2 == 0:
                                        print 'please enter ONLY ODD NUMBER!';
                                    if ten%2 == 1:
                                        if ten > MAX:
                                            MAX = ten;
                                        print MAX;

else:
     print 'please enter ONLY ODD NUMBER!';
