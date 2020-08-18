const Router = ReactRouterDOM.BrowserRouter;
const Route =  ReactRouterDOM.Route;
const Link =  ReactRouterDOM.Link;
const Prompt =  ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

function Homepage() {
    return <div> Welcome to my site </div>
}

function About() {
    return <div> Wine recommendation app </div>
}

function Login(props) {
  // a form with no logic yet
  return (
    <div>
      Username:
      <input type="text"></input>
      Password:
      <input type="text"></input>
      <button> Login </button>
    </div>
  )
}

function PostRecItem(props) {
  return <li>{props.rec}</li>
}

function Recommendation(props) {
  // get the info from the server
  // make componenets out of it
  // render them
  const [recList, setRecList] = React.useState(["loading..."])

  React.useEffect(() => {
    fetch('/api/recommendation')
    .then(res => res.json())
    .then((data) => {
      const recs = []
      for (const rec of data) {
        recs.push(<PostRecItem rec={rec}/>)
      }
      setRecList(recs)
    })
  }, [])

  return (
    <div>
      Here are some wines that match your criteria:
      <ul>
        {recList}
      </ul>
    </div>
  )
}


function App() {
  return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                  <Link to="/"> Home </Link>
              </li>
              <li>
                  <Link to="/about"> About </Link>
              </li>
              <li>
                  <Link to="/login"> Login </Link>
              </li>
              <li>
                  <Link to="/recommendation"> Wine Recommendation </Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/recommendation">
              <Recommendation />
            </Route>
            <Route path="/">
              <Homepage />
            </Route>

          </Switch>
        </div>
      </Router>
    );

}

ReactDOM.render(<App />, document.getElementById('root'))
