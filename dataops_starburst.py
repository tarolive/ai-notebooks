import sys
from sqlalchemy                import create_engine
from sqlalchemy.sql.expression import text
from trino.auth                import BasicAuthentication

connect_args = {
    'http_scheme' : 'https',
    'auth'        : BasicAuthentication(sys.argv[1], sys.argv[2])
}

engine = create_engine('trino://cloud-sample.trino.galaxy.starburst.io:443/sample/demo', connect_args = connect_args)
conn   = engine.connect()

astronauts = conn.execute(text('select * from astronauts limit 10')).fetchall()

for astronaut in astronauts:

    print(astronaut)
