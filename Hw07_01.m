% prob 1 and 2 combined
repeat = 'y';
while repeat~='Q'
    user_input= str2double(input('please enter class number','s'));
    if user_input==1
        fprintf('The corresponding class is "bard"');
    elseif user_input == 2
        fprintf('The corresponding class is "Cleric"');
    elseif user_input == 3
        fprintf('The corresponding class is "Durid"');
    elseif user_input == 4
        fprintf('The corresponding class is "Fighter"');
    elseif user_input == 5
        fprintf('The corresponding class is "Monk"')
    elseif user_input == 6
        fprintf('The corresponding class is "Paladin"');
    elseif user_input == 7
        fprintf('The corresponding class is "Ranger"')
    elseif user_input == 8
        fprintf('The corresponding class is "Rogue"')
    elseif user_input == 9
        fprintf('The corresponding class is "Sorcer"')
    elseif user_input == 10
        fprintf('The corresponding class is "Wizard"')
    elseif user_input == 11
        fprintf('The corresponding class is "Aberration"')    
    elseif user_input<0 || user_input>11
        fprintf('Please enter a number between 0 and 11');
    end
    repeat=('Please enterQ to quit or anything else to continue''s');
end

 



    






