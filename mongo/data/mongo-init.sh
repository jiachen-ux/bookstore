mongo -- "$MONGO_INITDB_DATABASE" <<EOF
db = db.getSiblingDB('admin')
db.auth('$MONGO_INITDB_ROOT_USERNAME', '$MONGO_INITDB_ROOT_PASSWORD')
db = db.getSiblingDB('$MONGO_INITDB_DATABASE')
db.createUser({
  user: "$MONGO_USERNAME",
  pwd: "$MONGO_PASSWORD",
  roles: [
  { role: 'readWrite', db: '$MONGO_INITDB_DATABASE' }
  ]
})
EOF

# #!/usr/bin/env bash
# echo "Creating mongo users..."
# mongo admin --host localhost -u root -p 123456 --eval "db.createUser({user: 'admin', pwd: '123456', roles: [{role: 'userAdminAnyDatabase', db: 'admin'}]});"
# mongo admin -u root -p 123456 << EOF
# use hi
# db.createUser({user: 'test', pwd: '123456', roles:[{role:'readWrite',db:'hi'}]})
# EOF
# echo "Mongo users created."