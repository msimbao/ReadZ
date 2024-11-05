# Importing required module
import subprocess

test = """
Once, there was a king who was on holiday. The king went to pick flowers with his friends. The king found a field of poppies, which were his favourite flower. He picked hundreds of poppies and forgot about his friends.

Many hours later, the king couldn’t find his friends. He was lost. The king was far away from his home, and all he had were the poppies he had picked. The king knew he could find the way home, but it would take a long time and he was thirsty. He needed water. The king thought, Hmm, maybe there is a river somewhere. He looked for a river, but then he saw a house on a hill. Ah! thought the king. I will ask for water at that house.

The king walked up the hill to the house. Outside the house, a young woman was working in the garden.

‘Hey there, young girl!’ said the king. ‘Could I ask you for some water? I have been picking poppies, and now I am very thirsty, and I must drink some water before finding my way back.’

‘Of course,’ said the woman. ‘But can I ask what a young man like you is doing picking poppies? Surely you have other work to do? Most men do not pick poppies for work.’

‘Ah!’ said the king. ‘I suppose I should say: I am a king.’

‘Oh!’ The woman bowed to the king. ‘I don’t know what country you come from, but it is wonderful to have you here. Would you like some pumpkin juice to drink?’

‘Pumpkin? What’s that?’ There were no pumpkins in the king’s country.

The woman showed the king some of her vegetables. ‘I grow pumpkins here, you see,’ she said. ‘That is my job.’

‘What a strange plant,’ said the king. ‘I have never seen anything like it. No, I would just like some water.’

‘You must eat some pumpkin before you leave this country,’ said the woman. ‘It is a very special vegetable. Ah, I will go get you some water.’

She bowed and went inside, and then came out looking very sad.

‘I’m sorry, but we only have one jug, and it is old and dirty.’ She showed him the jug, which was old and simple. ‘I do not think it is good enough for a king. You should have a gold jug with water from the highest mountain.’

‘No, no,’ said the king. ‘That jug is fine. The important thing is I am thirsty and I want to drink. I will be happy with that jug and your water.’

So the woman filled the jug with water and gave it to the king. But when the king finished drinking, she took the jug from his hands and threw it on the ground. SMASH! The jug broke into many pieces.

‘Well, that was strange,’ said the king. ‘Is this normal in your country? Should I break the jugs of my friends here?’

‘Well, well! You are a king, and so I wanted to give you a gold jug, but I could not. I could only give you an old and dirty jug. But now a king has used it, and so the jug is special. I do not want other people using that jug now – it is a king’s jug, and only a king can use it.’

The king did not say what he was thinking: the woman had broken the jug, so now nobody could use it. Not a king or a normal person. But he thought it was a lovely idea. He had been picking poppies, and when you pick a flower, it dies. Was it not the same with the jug? The jug was dead now, but he would remember drinking from it always.

‘Well, well,’ said the king. ‘This has been an interesting afternoon. I must go now, but I hope your pumpkins grow very big.’

‘Make sure to eat one before you leave!’ called the woman as he left.

The king stayed in that country for a month more, and he could not stop thinking about the woman. One night, his friend gave him pumpkin for supper, and the king liked the pumpkin very much. That night, he dreamed about the dirty old jug. There was something small inside the jug, and he could not see what it was. But the dream gave him an idea.

So before he went home, he sent a man to visit the woman. The man took a pumpkin and a jug with a small hole in the top. The hole was very small. If you tried to put your hand in the jug, only one finger would fit through the hole.

‘The king has a game for you,’ said the man. ‘You must put this pumpkin inside this jug. But you cannot break the jug or the pumpkin. Those are the rules.’

‘Oh no!’ said the woman. ‘How can I do such an impossible thing? The king will kill me!’

‘Ha!’ said the man. ‘He will not kill you. He is not a bad man. But he wants to see if you can do it. I’ve heard that you like breaking jugs. But there is no way this pumpkin will fit if you don’t break the jug!’

Of course, the man was right. It was an impossible game. The hole at the top of the jug was too small, and the pumpkin would not fit. If the woman broke the jug or the pumpkin, then she would break the rules.

But she thought for a while and said, ‘What do I get if I can fit the pumpkin in there?’

‘Just wait and see.’

The king returned to his country and months passed. He thought often of the pumpkin grower. In his home country, if a king wanted to marry a woman who was not the daughter of a king, he could normally not do it. But there was an old rule: if the king gave the woman an impossible job and she did it, then they could get married.

The king hoped very much that the woman could win his impossible game.

Later that year, the king went back to that country and visited the woman again.

‘Young girl! I’m here to see if you have a pumpkin jug for me.’

The woman heard the king’s voice and ran to him, holding the jug. She bowed quickly.

‘Look inside.’

The king looked inside, and yes! The pumpkin was inside the jug, and it was not broken.

‘You did it! And you did not break the rules. But how?’

‘Mm, first: what do I get?’

The king laughed. ‘Well, how would you like to grow pumpkins in my garden?’

‘That would be nice,’ said the woman. ‘But I can grow pumpkins here.’

‘Ah, but if we get married and you live here, it will be impossible!’

The pumpkin grower’s face went red. ‘Are you serious? You are really asking me to marry you?’

‘I would break a thousand jugs to show how serious I am.’

‘Then yes. A thousand times yes.’

So the king took her home and they prepared for the wedding. Every day, he asked her how she had done the impossible, but she wouldn’t tell him. Finally, a few days after they got married, she told him.

‘I took the seeds from your pumpkin and grew the plant. When the pumpkins were still small, I put one of them inside the jug and let it grow there. I had to make sure it got enough water and light, but it was quite easy, really.’

The king laughed. ‘So that was what I saw in my dream!’

‘Your dream?’

‘I dreamed that I saw something small inside a jug,’ said the king. ‘It must have been a seed.’ He kissed her. ‘I would like to learn to grow things, too, you know. I’ve never grown anything before.’

‘Well,’ said the queen. ‘Why don’t we grow some children?’

And they didn’t need a jug to do that!

THE END
"""
# Using system() method to
# execute shell commands
subprocess.Popen("echo '" + test + "' | piper \
  --model en_UK-jenny-tts \
  --output_file pumpkin.wav"
, shell=True)