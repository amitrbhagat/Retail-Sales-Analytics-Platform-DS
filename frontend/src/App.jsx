import {
  Routes,
  Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Analytics from "./pages/Analytics";
import Forecast from "./pages/Forecast";
import Inventory from "./pages/Inventory";
import Assistant from "./pages/Assistant";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";

import ProtectedRoute from "./components/ProtectedRoute";

function App() {

  return (

    <Routes>

      <Route

        path="/login"

        element={<Login />}

      />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/analytics"
        element={
          <ProtectedRoute>
            <Analytics />
          </ProtectedRoute>
        }
      />

      <Route
        path="/forecast"
        element={
          <ProtectedRoute>
            <Forecast />
          </ProtectedRoute>
        }
      />

      <Route
        path="/inventory"
        element={
          <ProtectedRoute>
            <Inventory />
          </ProtectedRoute>
        }
      />

      <Route
        path="/assistant"
        element={
          <ProtectedRoute>
            <Assistant />
          </ProtectedRoute>
        }
      />

      <Route
        path="/reports"
        element={
          <ProtectedRoute>
            <Reports />
          </ProtectedRoute>
        }
      />

      <Route
        path="/settings"
        element={
          <ProtectedRoute>
            <Settings />
          </ProtectedRoute>
        }
      />

    </Routes>

  );

}

export default App;