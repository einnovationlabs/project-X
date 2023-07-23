import './App.css';
import  DatasetPage  from "./components/Data/DatasetPage.js"

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to Project X

          <DatasetPage/>
        </p>
      </header>
    </div>
  );
}

export default App;
