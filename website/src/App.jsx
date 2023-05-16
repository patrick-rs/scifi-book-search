import './App.css'
import SearchComponent from './components/search'

const BASE_API_URL = 'http://127.0.0.1:5000'

function App() {

  return (
    <>
      <h1>Search</h1>
      <SearchComponent baseAPIUrl={BASE_API_URL} />
    </>
  )
}

export default App
