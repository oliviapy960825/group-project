from flask_script import Manager
from base import app, db, Movie, Genre

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    horror= Genre(name="Horror", description="Horror Films are unsettling films designed to frighten and panic, cause dread and alarm, and to invoke our hidden worst fears, often in a terrifying, shocking finale, while captivating and entertaining us at the same time in a cathartic experience.")
    action=Genre(name="Action", description="Action film is a genre in which the protagonist or protagonists end up in a series of challenges that typically include violence, extended fighting, physical feats, and frantic chases.")
    romantic=Genre(name="Romantic", description="Romance films or romance movies are romantic love stories recorded in visual media for broadcast in theaters and on TV that focus on passion, emotion, and the affectionate romantic involvement of the main characters and the journey that their genuinely strong, true and pure romantic love takes them through dating, courtship or marriage.")
    split=Movie(name="Split", director="M. Night Shyamalan", actors="James McAvoy, Anya Taylor-Joy, Betty Buckley, Haley Lu Richardson", description="Split is a 2016 American psychological horror-thriller film written and directed by M. Night Shyamalan and starring James McAvoy, Anya Taylor-Joy, and Betty Buckley. The film follows a man with 23 different personalities who kidnaps and imprisons three teenage girls in an isolated underground facility.", genre=horror)
    darkKnight=Movie(name="The Dark Knight", director=" Christopher Nolan", actors=" Christian Bale, Heath Ledger, Aaron Eckhart", description="When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.", genre=action)
    titanic=Movie(name="Titanic", director="James Cameron", actors=" Leonardo DiCaprio, Kate Winslet, Billy Zane", description="A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.", genre=romantic)
    db.session.add(horror)
    db.session.add(action)
    db.session.add(romantic)
    db.session.add(split)
    db.session.add(darkKnight)
    db.session.add(titanic)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
