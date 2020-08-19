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

// function Selector(props) {

//   function onChange(e) {
//     this.value = e.target.value
//   }
//   return (
//     <div>
//       <select onChange={self.onChange}>
//         {props.optionsList.map(option => {
//           return <option value={option}> option </option>;
//         }
//       </select>
//     </div>
//   )
// }

function Recommendation(props) {

  const [minYear, setMinYear] = React.useState('1000')
  const [maxYear, setMaxYear] = React.useState('2017')
  const [minPrice, setMinPrice] = React.useState('0')
  const [maxPrice, setMaxPrice] = React.useState('3300')
  const [descriptor, setDescriptor] = React.useState([])
  const [recList, setRecList] = React.useState(["loading..."])
  const [showResult, setShowResult] = React.useState(false)

  const WineFilters = (e)=> {
    e.preventDefault()
    const filters = {"min_year": minYear,
                    "max_year": maxYear,
                    "min_price": minPrice,
                    "max_price": maxPrice,
                    "descriptor": descriptor}
    console.log(filters)
    console.log(JSON.stringify(filters))
    fetch('/api/recommendation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(filters),
    })
    .then(res => res.json())
    .then((data) => {
      const recs = []
      for (const rec of data) {
        recs.push(<PostRecItem rec={rec}/>)
      }
      setRecList(recs)
      setShowResult(true)
    })
  }

  function WineResult() {
    if (showResult) {
      return (
        <div>
          Here are some wines that match your criteria:
          <ul>
            {recList}
          </ul>
        </div>
      )
    }
    {
      return (
        <form onSubmit={WineFilters} id="wine-search" method="POST">
          <div>
            Please pick your year of production range(optional):
            Min:
            {/* <Selector options=[1970, 1980, 1990, 2000] id="min-year" /> */}
            <select value={minYear} onChange={(e) => setMinYear(e.target.value)} id="min-year" name="min-year">
              <option value="1970">1970</option>
              <option value="1980">1980</option>
              <option value="1990">1990</option>
              <option value="2000">2000</option>
            </select>
            Max:
            <select value={maxYear} onChange={(e) => setMaxYear(e.target.value)} id="max-year" name="max-year">
              <option value="2017">2017</option>
              <option value="2015">2015</option>
              <option value="2013">2013</option>
              <option value="2011">2011</option>
            </select>
          </div>
          <div>
            Please pick your price range:
            Min:
            <select value={minPrice} onChange={(e) => setMinPrice(e.target.value)} id="min-price" name="min-price">
              <option value="0">0</option>
              <option value="10">10</option>
              <option value="20">20</option>
              <option value="30">30</option>
              <option value="40">40</option>
              <option value="50">50</option>
              <option value="60">60</option>
              <option value="70">70</option>
            </select>
            Max:
            <select value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} id="max-price" name="max-price">
              <option value="10">10</option>
              <option value="20">20</option>
              <option value="30">30</option>
              <option value="40">40</option>
              <option value="50">50</option>
              <option value="60">60</option>
              <option value="70">70</option>
              <option value="1000">1000</option>
            </select>
          </div>
          <div>
            Please choose descriptors for your dream wine:
            <input value={descriptor} onChange={(e) => setDescriptor(e.target.value)} type="checkbox" className="descriptor" name="descriptor" value="cherry"/>cherry
            <input type="checkbox" className="descriptor" name="descriptor" value="strawberry"/>strawberry
            <input type="checkbox" className="descriptor" name="descriptor" value="mushroom"/>mushroom
            <input type="checkbox" className="descriptor" name="descriptor" value="oak"/>oak
            <input type="checkbox" className="descriptor" name="descriptor" value="ripe"/>ripe
            <input type="checkbox" className="descriptor" name="descriptor" value="perfumed"/>perfumed
            <input type="checkbox" className="descriptor" name="descriptor" value="juicy"/>juicy
          </div>

          <input type="submit"/>
        </form>
      )
    }
  };


  return (
    <WineResult />
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
