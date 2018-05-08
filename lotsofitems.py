from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="im Robot", email="fakeuser@gmail.com")
session.add(User1)
session.commit()

# Create category of Action Films
category1 = Categories(name="Action")
session.add(category1)
session.commit()


# Create category of Adventure Films
category2 = Categories(name="Adventure")
session.add(category2)
session.commit()

# Create category of Comedy Films
category3 = Categories(name="Comedy")
session.add(category3)
session.commit()

# Create category of Drama Films
category4 = Categories(name="Drama")
session.add(category4)
session.commit()

# Create category of History Films
category5 = Categories(name="History")
session.add(category5)
session.commit()

# Create category of Military Films
category6 = Categories(name="Military")
session.add(category6)
session.commit()

# Create category of Musicals Films
category7 = Categories(name="Musicals")
session.add(category7)
session.commit()

# Create category of Romance Films
category8 = Categories(name="Romance")
session.add(category8)
session.commit()

# Create category of Science Fiction Films
category9 = Categories(name="Science Fiction")
session.add(category9)
session.commit()



# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="West Side Story",
                             description="Two youngsters from rival New York\
                              City gangs fall in love, but tensions between \
                              their respective friends build toward tragedy.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Silence of the Lambs",
                             description="A young F.B.I. cadet must confide in\
                              an incarcerated and manipulative killer to \
                              receive his help on catching another serial \
                              killer who skins his victims.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Saving Private Ryan",
                             description="Saving Private Ryan is a 1998 American\
                              epic drama war film set during the Invasion of\
                               Normandy in World War II. .",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Deer Hunter",
                             description="The Deer Hunter is a 1978 American\
                              epic war drama film co-written and directed by\
                               Michael Cimino about a trio of Russian American\
                                steelworkers and their service in the Vietnam War.",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Scarface",
                             description="In Miami in 1980, a determined\
                              Cuban immigrant takes over a drug cartel \
                              and succumbs to greed.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Secret Life of Pets",
                             description="The quiet life of a terrier \
                             named Max is upended when his owner takes \
                             in Duke, a stray whom Max instantly dislikes.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dance Academy: The Movie",
                             description="This 2017 movie follows the \
                             original dance academy TV show and tracks \
                             where the characters are in their lives now.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Jerry Maguire",
                             description="Jerry Maguire is a man who knows\
                              the score. As a top agent at Sports Management\
                               International, Jerry is unquestionably a\
                                master of his universe.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Hidden Figures",
                             description="The story of a team of female\
                              African-American mathematicians who served\
                               a vital role in NASA during the early years\
                                of the U.S. space program.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="300",
                             description="King Leonidas of Sparta and a force\
                              of 300 men fight the Persians at Thermopylae in\
                               480 B.C.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Martian",
                             description="An astronaut becomes stranded on \
                             Mars after his team assume him dead, and must \
                             rely on his ingenuity to find a way to signal \
                             to Earth that he is alive.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Kingsman: The Golden Circle",
                             description="When their headquarters are \
                             destroyed and the world is held hostage, \
                             the Kingsman's journey leads them to the \
                             discovery of an allied spy organization in \
                             the US. These two elite secret organizations \
                             must band together to defeat a common enemy.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Godfather",
                             description="The aging patriarch of an organized\
                              crime dynasty transfers control of his \
                              clandestine empire to his reluctant son.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Atonement",
                             description="In 1935, 13-year-old fledgling writer\
                              Briony Tallis and her family live a life of wealth\
                               and privilege in their enormous mansion.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dunkirk",
                             description="Allied soldiers from Belgium, \
                             the British Empire and France are surrounded\
                              by the German Army, and evacuated during a \
                              fierce battle in World War II.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Titanic",
                             description="A seventeen-year-old aristocrat\
                             falls in love with a kind but poor artist \
                             aboard the luxurious, ill-fated R.M.S. Titanic.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Star Wars: The Last Jedi",
                             description="Having taken her first steps into\
                              a larger world in Star Wars: The Force Awakens\
                               (2015), Rey continues her epic journey with \
                               Finn, Poe, and Luke Skywalker in the next \
                               chapter of the saga.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Deadpool",
                             description="A fast-talking mercenary with \
                             a morbid sense of humor is subjected to a rogue\
                              experiment that leaves him with accelerated \
                              healing powers and a quest for revenge.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                             name="Pirates of the Caribbean: \
                             Dead Men Tell No Tales",
                             description="Captain Jack Sparrow searches \
                             for the trident of Poseidon while being pursued\
                              by an undead sea captain and his crew.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="It",
                             description="A group of bullied kids band \
                             together when a shapeshifting demon, taking \
                             the appearance of a clown, begins hunting \
                             children.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Despicable Me 3",
                             description="Gru meets his long-lost charming,\
                              cheerful, and more successful twin brother Dru\
                               who wants to team up with him for one last\
                                criminal heist.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

print "added category items!"
