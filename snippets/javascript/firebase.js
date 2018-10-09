import firebase from 'firebase/app'
import 'firebase/firestore'
import 'firebase/auth'

const config = {
  // Project info here...
}

if (!firebase.apps.length) firebase.initializeApp(config)

export const firestore = firebase.firestore()
export const auth = firebase.auth()
export const authPersist = firebase.auth.Auth.Persistence.LOCAL
export const functions =
  `https://us-central1-${config.projectId}.cloudfunctions.net/`

firestore.settings({ timestampsInSnapshots: true })

export default firebase
