// check cookie for `logged_in` substring (this only works for insecure cookies. Not http-only)
const isLoggedIn = () => document.cookie.includes('logged_in')

// check cookie for changes when you open this tab
const signInSpy = () => {
  document.visibilitystate === 'visible' &&
    isLoggedIn() &&
    alert('refresh, please')
}

// only attach event handler when not signed in.
document.onvisibilitychange = isLoggedIn() ? null : signInSpy