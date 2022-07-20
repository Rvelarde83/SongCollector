# SongCollector

## app for the songwriter

- App designed for whoever is keeping track of the creative endeaver known as writing a song, keep track of whoever is collaborating, producing, recording, etc...
Write notes and add media to the record of the song, 

Maybe focus the app more for the songwriter? more about the sections, verses, chorus, bridge?
Same thing with progressions?

right now I need to write the model of the song and continue from the lessons over here:
https://seir-222-sasquatch.netlify.app/second-language/week-20/day-3/lecture-materials/intro-to-django-models/    

https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html



be able to add pictures of users using amazon and of the musicians and users? ???
then CSS

relation ship
song to user, one tomany, one user, many songs
songs musicians many to many
needing pictures
? 

needing to fix musicians_detail, that's what broken
musicians on song index have a link to musicans


{% for musician in musician_list %}
  <a href="{% url 'musicians_detail' musician.id %}">
    <div class="card">
        <div class="card-content">
            <span class="card-title">{{ musician.name }}</span>
            <p>Instrument: {{ musician.instrument }}</p>
        </div>
    </div>
  </a>
{% endfor %}

{% endblock %}
