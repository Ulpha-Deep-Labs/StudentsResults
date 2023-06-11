import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

import {
	createBrowserRouter,
	RouterProvider,
	Navigate,
} from "react-router-dom";
import Login from "./pages/Login";

const router = createBrowserRouter([
	{
		path: "/login",
		element: <Login />,
	},
	{
		path: "/",
		element: <Navigate to={"/login"} />,
	},
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>
);
