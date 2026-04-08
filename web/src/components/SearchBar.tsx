"use client";

type SearchBarProps = {
  value: string;
  placeholder?: string;
  onChange: (value: string) => void;
};

export function SearchBar({
  value,
  placeholder = "Search papers, topics, or authors",
  onChange,
}: SearchBarProps) {
  return (
    <label className="searchBar">
      <span>Search</span>
      <input
        type="search"
        value={value}
        placeholder={placeholder}
        onChange={(event) => onChange(event.target.value)}
      />
    </label>
  );
}
