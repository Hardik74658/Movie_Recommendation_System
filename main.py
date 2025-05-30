import streamlit as st
import pickle
# Load data
movies = pickle.load(open('movie_list (1).pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append("https://image.tmdb.org/t/p/w500/"+(movies[movies['id'] == movie_id]['poster_path'].values[0]))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

def main():
    # st.write(movies)
    # Page config and title
    st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="wide")
    st.title("🎬 Movie Recommender System")

 

    # Movie selection dropdown with search
    movie_list = movies['title'].values
    st.subheader("Select a Movie to Get Recommendations")
    selected_movie = st.selectbox("",movie_list)

    # Recommendation button
    if st.button("Show Recommendations"):
        with st.spinner("Fetching recommendations..."):
            names, posters = recommend(selected_movie)
        
        # Display recommendations in 5 columns
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            col.markdown(f"**{names[idx]}**")
            col.image(posters[idx], use_container_width=True)

    # Add footer or credits
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align:center; font-size:12px; color:gray;">
            Powered by TMDB API and Streamlit | Developed by Hardik Songara
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
