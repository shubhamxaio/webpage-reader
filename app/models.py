from app import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), index=True, unique=True)
    crwalled = db.Column(db.Boolean, default=False)
    total_words = db.Column(db.Integer, default=0)

    def create_entry(self, url):
        try:
            u = URL(url=url)
            db.session.add(u)
            db.session.commit()
            return True
        except Exception as exception:
            print(exception)
        return False

    def update_total_words(self, id, total_words):
        u = URL.query.filter_by(id=id).update(dict(total_words=total_words))
        db.session.commit()

    def __repr__(self):
        return '<URL {}>'.format(self.url)
