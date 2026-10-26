// Noms de pays en fr / en / es / ar (26/10/2026), pour le chercheur de centres (make_gazetteer.py).
// Foundation seulement, rien à télécharger : swift _build/country_names.swift > _build/data/country_names.json
import Foundation

let langs = ["fr", "en", "es", "ar"]
let locs = langs.map { Locale(identifier: $0) }
var out: [String: [String: String]] = [:]
for code in Locale.isoRegionCodes where code.count == 2 && code.allSatisfy({ $0.isLetter }) {
    var names: [String: String] = [:]
    for (l, loc) in zip(langs, locs) {
        if let n = loc.localizedString(forRegionCode: code) { names[l] = n }
    }
    if names.count == langs.count { out[code] = names }
}
let data = try! JSONSerialization.data(withJSONObject: out, options: [.sortedKeys])
FileHandle.standardOutput.write(data)
FileHandle.standardOutput.write("\n".data(using: .utf8)!)
